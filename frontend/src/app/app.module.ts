import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import {SearchBarComponent} from "./components/search-bar/search-bar.component";
import {ReactiveFormsModule} from "@angular/forms";
import { addItemComponent } from "./components/addItem/addItem.component";
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
/*import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';*/

@NgModule({
    declarations: [
        AppComponent,
        SearchBarComponent,
      addItemComponent
    ],
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    FontAwesomeModule,
    /*FontAwesomeModule*/
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
