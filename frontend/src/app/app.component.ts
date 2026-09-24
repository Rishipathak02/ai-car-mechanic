import {
  Component,
  inject,
  ChangeDetectorRef
} from '@angular/core';

import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { ApiService } from './services/api.service';


type Msg = {
  role: 'user' | 'assistant';
  text: string;
};


@Component({
  selector: 'app-root',
  standalone: true,

  imports: [
    CommonModule,
    FormsModule
  ],

  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})


export class AppComponent {

  private api = inject(ApiService);

  private cdr = inject(ChangeDetectorRef);


  // =========================
  // SESSION
  // =========================

  sessionId = crypto.randomUUID();


  // =========================
  // CHAT
  // =========================

  input = '';

  loading = false;


  // =========================
  // DIAGNOSIS
  // =========================

  diagnosis = '';

  recommendation = '';


  // =========================
  // BOOKING
  // =========================

  showBooking = false;


  booking = {

    name: '',

    phone: '',

    car_model: '',

    issue: '',

    preferred_date: '',

    preferred_time: ''

  };


  // =========================
  // MESSAGES
  // =========================

  messages: Msg[] = [

    {

      role: 'assistant',

      text:
        'Hello! I am your AI Car Mechanic. Tell me what is wrong with your car.'

    }

  ];


  // =====================================================
  // SEND CHAT MESSAGE
  // =====================================================

  send() {

    const text = this.input.trim();


    if (!text || this.loading) {

      return;

    }


    // Add user message

    this.messages.push({

      role: 'user',

      text: text

    });


    // Clear input

    this.input = '';


    // Show loading

    this.loading = true;


    this.cdr.detectChanges();


    // Call backend

    this.api.chat({

      session_id: this.sessionId,

      message: text

    })

    .subscribe({

      next: (response) => {

        setTimeout(() => {


          // Add AI response

          this.messages.push({

            role: 'assistant',

            text: response.reply

          });


          this.loading = false;


          this.cdr.detectChanges();


        }, 1500);

      },


      error: () => {


        this.messages.push({

          role: 'assistant',

          text:
            'Server error. Please make sure FastAPI is running.'

        });


        this.loading = false;


        this.cdr.detectChanges();

      }

    });

  }


  // =====================================================
  // FILE SELECT
  // =====================================================

  fileSelected(event: Event) {


    const input =
      event.target as HTMLInputElement;


    const file =
      input.files?.[0];


    if (!file) {

      return;

    }


    // =================================================
    // IMAGE
    // =================================================

    if (file.type.startsWith('image/')) {


      this.loading = true;


      this.messages.push({

        role: 'assistant',

        text:
          'Image received. AI is analyzing your car image...'

      });


      this.cdr.detectChanges();


      // Call AI image diagnosis API

      this.api.imageDiagnosis(

        this.sessionId,

        file

      )

      .subscribe({

        next: (response) => {


          // Store diagnosis

          this.diagnosis =
            response.diagnosis;


          // Recommendation

          this.recommendation =
            'Please follow the safety recommendations provided by the AI and consult a qualified mechanic if required.';


          // Add diagnosis to chat

          this.messages.push({

            role: 'assistant',

            text: response.diagnosis

          });


          this.loading = false;


          this.cdr.detectChanges();

        },


        error: (error) => {


          console.error(
            'Image diagnosis error:',
            error
          );


          this.messages.push({

            role: 'assistant',

            text:
              'AI image diagnosis failed. Please check that FastAPI and Gemini are running.'

          });


          this.loading = false;


          this.cdr.detectChanges();

        }

      });


      return;

    }


    // =================================================
    // AUDIO / VIDEO
    // =================================================

    this.api.upload(

      this.sessionId,

      file

    )

    .subscribe({

      next: (response) => {


        this.messages.push({

          role: 'assistant',

          text:
            `Media uploaded successfully: ${response.filename}`

        });


        this.cdr.detectChanges();

      },


      error: () => {


        this.messages.push({

          role: 'assistant',

          text:
            'Media upload failed.'

        });


        this.cdr.detectChanges();

      }

    });

  }


  // =====================================================
  // TEXT DIAGNOSIS
  // =====================================================

  runDiagnosis() {


    const symptoms = this.messages

      .filter(
        message =>
          message.role === 'user'
      )

      .map(
        message =>
          message.text
      )

      .join('\n');


    if (!symptoms) {

      return;

    }


    this.loading = true;


    this.cdr.detectChanges();


    // Call diagnosis API

    this.api.diagnosis({

      session_id:
        this.sessionId,

      symptoms:
        symptoms

    })

    .subscribe({

      next: (response) => {


        this.diagnosis =
          response.diagnosis;


        this.recommendation =
          response.recommendation;


        this.loading = false;


        this.cdr.detectChanges();

      },


      error: (error) => {


        console.error(
          'Diagnosis error:',
          error
        );


        this.loading = false;


        this.cdr.detectChanges();

      }

    });

  }


  // =====================================================
  // FORMAT AI DIAGNOSIS
  // =====================================================

  formatDiagnosis(
    text: string
  ): string {


    if (!text) {

      return '';

    }


    let html = text;


    // ---------------------------------
    // Escape HTML
    // ---------------------------------

    html = html

      .replace(
        /&/g,
        '&amp;'
      )

      .replace(
        /</g,
        '&lt;'
      )

      .replace(
        />/g,
        '&gt;'
      );


    // ---------------------------------
    // Markdown headings
    // ---------------------------------

    html = html.replace(

      /^###\s*(.+)$/gm,

      '<h3>$1</h3>'

    );


    // ---------------------------------
    // Bold text
    // ---------------------------------

    html = html.replace(

      /\*\*(.*?)\*\*/g,

      '<strong>$1</strong>'

    );


    // ---------------------------------
    // Bullet points
    // ---------------------------------

    html = html.replace(

      /^\s*\*\s+(.*)$/gm,

      '<li>$1</li>'

    );


    // ---------------------------------
    // Convert bullet groups
    // ---------------------------------

    html = html.replace(

      /((?:<li>.*?<\/li>\s*)+)/gs,

      '<ul>$1</ul>'

    );


    // ---------------------------------
    // Numbered list
    // ---------------------------------

    html = html.replace(

      /^\s*(\d+)\.\s+(.*)$/gm,

      '<p><strong>$1.</strong> $2</p>'

    );


    // ---------------------------------
    // Line breaks
    // ---------------------------------

    html = html.replace(

      /\n/g,

      '<br>'

    );


    return html;

  }


  // =====================================================
  // OPEN BOOKING
  // =====================================================

  openBooking() {


    this.booking.issue =
      this.diagnosis;


    this.showBooking =
      true;


    this.cdr.detectChanges();

  }


  // =====================================================
  // SUBMIT BOOKING
  // =====================================================

  submitBooking() {


    this.api.booking(

      this.booking

    )

    .subscribe({

      next: (response) => {


        alert(

          `Booking #${response.booking_id} created successfully`

        );


        this.showBooking =
          false;


        // Reset booking form

        this.booking = {

          name: '',

          phone: '',

          car_model: '',

          issue: '',

          preferred_date: '',

          preferred_time: ''

        };


        this.cdr.detectChanges();

      },


      error: (error) => {


        console.error(
          'Booking error:',
          error
        );


        alert(
          'Booking failed. Please try again.'
        );

      }

    });

  }

}