import { Component, Inject, computed, signal, ɵɵtrustConstantHtml } from "@angular/core";
import { MatButtonModule } from "@angular/material/button";
import { MatInputModule } from "@angular/material/input";
import { MatFormFieldModule } from "@angular/material/form-field";
import { MatIconModule } from "@angular/material/icon";
import { MatCardModule } from "@angular/material/card";
import { AwardSearchService } from "../award-search.service";

@Component({
  selector: "app-award-search",
  standalone: true,
  templateUrl: "./award-search.component.html",
  styleUrl: "./award-search.component.scss",
  imports: [MatButtonModule, MatInputModule, MatFormFieldModule, MatIconModule, MatCardModule],
})
export class AwardSearchComponent {
  readonly smartChat = computed(() => this.awardSearchService.smartChat());
  readonly activeChat = computed(() => this.awardSearchService.activeChat());

  constructor(private awardSearchService: AwardSearchService) {}

  sendPrompt(prompt: string) {
    console.log(prompt);

    this.awardSearchService.sendPrompt(prompt);
  }
}
