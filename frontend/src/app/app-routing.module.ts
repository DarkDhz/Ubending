import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LogInSignUpComponent } from "./components/log-in-sign-up/log-in-sign-up.component";
import {UserProductsComponent} from "./components/user-products/user-products.component";
import {HomeComponent} from "./components/home/home.component";

const routes: Routes = [
  { path: '', redirectTo: '/login-signup',pathMatch: 'full'},
  { path: 'login-signup', component: LogInSignUpComponent},
  { path: 'user-products', component: UserProductsComponent},
  { path: 'home', component: HomeComponent}
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
export  const routingComponents = [LogInSignUpComponent,UserProductsComponent, HomeComponent]
