import { Component, signal } from "@angular/core";
import { RouterOutlet } from "@angular/router";
import { MatButtonModule } from "@angular/material/button";
import { MatMenuModule } from "@angular/material/menu";
import { MatToolbarModule } from "@angular/material/toolbar";
import { MatIconModule } from "@angular/material/icon";
import { MatDividerModule } from "@angular/material/divider";
import { MatListModule } from "@angular/material/list";

@Component({
  selector: "app-root",
  standalone: true,
  templateUrl: "./app.component.html",
  styleUrl: "./app.component.scss",
  imports: [RouterOutlet, MatButtonModule, MatMenuModule, MatToolbarModule, MatIconModule, MatDividerModule, MatListModule],
})
export class AppComponent {
  title = "client";

  isDarkmode = signal<boolean>(false);

  constructor() {}

  toggleTheme() {
    this.isDarkmode.set(!this.isDarkmode());
  }
}
