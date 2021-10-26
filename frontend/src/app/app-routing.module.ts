import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LogInSignUpComponent } from "./components/log-in-sign-up/log-in-sign-up.component";
import { SearchBarComponent } from "./components/search-bar/search-bar.component";
import {UserProductsComponent} from "./components/user-products/user-products.component";

const routes: Routes = [
  { path: '', redirectTo: '/login-signup',pathMatch: 'full'},
  { path: 'login-signup', component: LogInSignUpComponent},
  { path: 'user-products', component: UserProductsComponent}
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes)
  ],
  exports: [
    RouterModule
  ]
})
export class AppRoutingModule { }
export  const routingComponents = [LogInSignUpComponent, SearchBarComponent]
