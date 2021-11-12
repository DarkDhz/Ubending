import { Component, OnInit } from '@angular/core';
import {FormControl, FormGroup, Validators} from "@angular/forms";

@Component({
  selector: 'app-reset-password',
  templateUrl: './reset-password.component.html',
  styleUrls: ['./reset-password.component.css']
})
export class ResetPasswordComponent implements OnInit {
  showAlertDifferentPasswords: Boolean = false;
  showAlertInvalid: Boolean = false;
  resetPasswordForm = new FormGroup({
    newPassword: new FormControl('', Validators.required),
    passwordConfirm: new FormControl('', Validators.required)
  })

  constructor() { }

  ngOnInit(): void {
  }

  get password1(){
    return this.resetPasswordForm.get('newPassword')
  }

  get password2(){
    return this.resetPasswordForm.get('passwordConfirm')
  }

  validatePasswords(){
    if (this.password1?.value != this.password2?.value){
      this.showAlertInvalid = false;
      this.showAlertDifferentPasswords = true;

    } else{
      if (this.password1!.errors?.required) {
        this.showAlertDifferentPasswords = false;
        this.showAlertInvalid = true;
      } else{
        this.showAlertDifferentPasswords = false;
        this.showAlertInvalid = false;
        this.onClickReset()
      }
    }
  }

  onClickHome(){
    // @ts-ignore
    this.$router.replace({path: '/', query: {}})
  }

  onClickReset(){
    // @ts-ignore
    this.$router.replace({path: '/login-signup', query: {}})
  }

}
