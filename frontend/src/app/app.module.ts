import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import {SearchBarComponent} from "./components/search-bar/search-bar.component";
import {ReactiveFormsModule} from "@angular/forms";
import { addItemComponent } from "./components/addItem/addItem.component";
import { AppRoutingModule, routingComponents } from "./app-routing.module";
import { UserProductsComponent } from './components/user-products/user-products.component';

/*import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';*/

@NgModule({
  declarations: [
    AppComponent,
    SearchBarComponent,
    addItemComponent,
    routingComponents,
    UserProductsComponent
    ],
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    AppRoutingModule
    /*FontAwesomeModule*/
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
