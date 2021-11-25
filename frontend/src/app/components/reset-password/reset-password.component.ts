import { Component, OnInit } from '@angular/core';
import {FormControl, FormGroup, Validators} from "@angular/forms";
import {ActivatedRoute, Router} from "@angular/router";
import axios from "axios";

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

  token: string | null = 'null';

  constructor(private route: ActivatedRoute, private router: Router) { }

  ngOnInit(): void {
    this.token = this.route.snapshot.paramMap.get('token');
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
    const path = `https://ubending4.herokuapp.com/reset_password/` + this.token

    const params = {
      password: (<HTMLInputElement>document.getElementById("newPassword")).value,
      repeat_password: (<HTMLInputElement>document.getElementById("passwordConfirm")).value
    }

    // here send email
    axios.post(path, params).then((res) => {
      this.router.navigate(['/login-signup']);
      })
      .catch((error) => {
        console.error(error)
        alert(error.response.data.message)
      })
  }

}
