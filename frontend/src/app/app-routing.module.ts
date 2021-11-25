import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { LogInSignUpComponent } from "./components/log-in-sign-up/log-in-sign-up.component";
import {UserProductsComponent} from "./components/user-products/user-products.component";
import {HomeComponent} from "./components/home/home.component";
import {RecoverPasswordComponent} from "./components/recover-password/recover-password.component";
import {ResetPasswordComponent} from "./components/reset-password/reset-password.component";
import { ProfileComponent } from './profile/profile.component';


const routes: Routes = [
  { path: '', redirectTo: '/home',pathMatch: 'full'},
  { path: 'login-signup', component: LogInSignUpComponent},
  { path: 'user-products', component: UserProductsComponent},
  { path: 'home', component: HomeComponent},
  { path: 'recover', component: RecoverPasswordComponent},
  { path: 'reset/:token', component: ResetPasswordComponent},
  { path: 'user-profile', component: ProfileComponent}
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
export  const routingComponents = [LogInSignUpComponent,UserProductsComponent,
                                    HomeComponent, RecoverPasswordComponent, ResetPasswordComponent]
