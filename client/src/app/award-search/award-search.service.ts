import { Injectable, computed, effect, signal } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { catchError, firstValueFrom } from "rxjs";
import { chatMessage } from "./award-search";

@Injectable({
  providedIn: "root",
})
export class AwardSearchService {
  private api_endpoint = "api.endpoint";

  private _smartChat = signal<chatMessage[]>([
    { type: "src", text: "I want to submit a proposal about animal sounds" },
    { type: "res", text: "I want to submit a proposal about animal sounds1" },
    { type: "src", text: "I want to submit a proposal about animal sounds2" },
    { type: "res", text: "I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3I want to submit a proposal about animal sounds3" },
  ]);
  readonly smartChat = this._smartChat.asReadonly();

  readonly activeChat = computed(() => this._smartChat.length > 0)

  constructor(private http: HttpClient) {
    effect(() => {
      console.log(this.smartChat());
      
    })
  }

  async sendPrompt(prompt: string) {
    const url = `${this.api_endpoint}/endpoint`;

    await this._postRequest(prompt, url);
  }

  async _postRequest(text: string, url: string) {
    try {
      // Await the result of the HTTP POST call
      const result = await firstValueFrom(this.http.post<any>(url, text).pipe());
      // Return the resulting object on success
      return result;
    } catch (error) {
      // If an error is caught, log it and throw it again if needed
      console.error("Error in postData:", error);
      throw error; // Optionally rethrow the error
    }
  }
}