import { Component } from "@angular/core";
import { MatButtonModule } from "@angular/material/button";
import { MatInputModule } from "@angular/material/input";
import { MatFormFieldModule } from "@angular/material/form-field";
import { MatIconModule } from "@angular/material/icon";

@Component({
  selector: "app-award-search",
  standalone: true,
  templateUrl: "./award-search.component.html",
  styleUrl: "./award-search.component.scss",
  imports: [MatButtonModule, MatInputModule, MatFormFieldModule, MatIconModule],
})
export class AwardSearchComponent {

  sendPrompt(prompt: string) {
    console.log(prompt);
    
  }
}
