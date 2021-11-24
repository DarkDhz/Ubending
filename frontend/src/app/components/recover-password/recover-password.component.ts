import { Component, OnInit } from '@angular/core';
import axios from 'axios'
import { FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-recover-password',
  templateUrl: './recover-password.component.html',
  styleUrls: ['./recover-password.component.css']
})
export class RecoverPasswordComponent implements OnInit {
  showEmailSent: Boolean = false;
  showAlertRequired: Boolean = false;
  showAlertInvalid: Boolean = false;
  userEmail = new FormGroup({
    email: new FormControl('', [
      Validators.required,
      Validators.pattern("^[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$")])
  });

  constructor() { }

  ngOnInit(): void {

  }

  get emailUser(){
    return this.userEmail.get('email')
  }

  validateEmail(){
    if (!this.emailUser!.errors?.required && !this.emailUser!.errors?.pattern) {
      this.showAlertInvalid = false;
      this.showAlertRequired = false;
      this.showEmailSent = true;
    } else {
      if (this.emailUser!.errors?.required ) {
        this.showAlertInvalid = false;
        this.showEmailSent = false;
        this.showAlertRequired = true;

      } else if (this.emailUser!.errors?.pattern) {
        this.showEmailSent = false;
        this.showAlertRequired = false;
        this.showAlertInvalid = true;
      }
    }
  }


onClickHome(){
    // @ts-ignore
    this.$router.replace({path: '/', query: {}})
  }

  onClickCancel(){
    // @ts-ignore
    this.$router.replace({path: '/', query: {}})
  }

}
