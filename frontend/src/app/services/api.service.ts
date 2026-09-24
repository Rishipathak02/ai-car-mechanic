import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private http = inject(HttpClient);

  private base = 'http://localhost:8000/api';


  // =========================
  // CHAT
  // =========================

  chat(
    data: {
      session_id: string;
      message: string;
    }
  ): Observable<{ reply: string }> {

    return this.http.post<{ reply: string }>(
      `${this.base}/chat/`,
      data
    );
  }


  // =========================
  // TEXT DIAGNOSIS
  // =========================

  diagnosis(
    data: {
      session_id: string;
      symptoms: string;
    }
  ): Observable<{
    diagnosis: string;
    recommendation: string;
  }> {

    return this.http.post<{
      diagnosis: string;
      recommendation: string;
    }>(
      `${this.base}/diagnosis/`,
      data
    );
  }


  // =========================
  // MEDIA UPLOAD
  // =========================

  upload(
    sessionId: string,
    file: File
  ): Observable<{
    url: string;
    filename: string;
  }> {

    const fd = new FormData();

    fd.append('session_id', sessionId);
    fd.append('file', file);

    return this.http.post<{
      url: string;
      filename: string;
    }>(
      `${this.base}/upload/`,
      fd
    );
  }


  // =========================
  // AI IMAGE DIAGNOSIS
  // =========================

  imageDiagnosis(
    sessionId: string,
    file: File
  ): Observable<{
    session_id: string;
    filename: string;
    diagnosis: string;
    image_url: string;
  }> {

    const fd = new FormData();

    fd.append('session_id', sessionId);
    fd.append('file', file);

    return this.http.post<{
      session_id: string;
      filename: string;
      diagnosis: string;
      image_url: string;
    }>(
      `${this.base}/image-diagnosis/`,
      fd
    );
  }


  // =========================
  // BOOKING
  // =========================

  booking(
    data: Record<string, string>
  ): Observable<{
    booking_id: number;
    status: string;
    message: string;
  }> {

    return this.http.post<{
      booking_id: number;
      status: string;
      message: string;
    }>(
      `${this.base}/booking/`,
      data
    );
  }
}
