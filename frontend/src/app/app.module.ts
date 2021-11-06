import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import {SearchBarComponent} from "./components/search-bar/search-bar.component";
import {ReactiveFormsModule} from "@angular/forms";
import { addItemComponent } from "./components/addItem/addItem.component";
import { DeleteItemComponent } from "./components/delete-item/delete-item.component";

/*import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';*/

@NgModule({
    declarations: [
        AppComponent,
      DeleteItemComponent,
        SearchBarComponent,
      addItemComponent
    ],
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    /*FontAwesomeModule*/
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
