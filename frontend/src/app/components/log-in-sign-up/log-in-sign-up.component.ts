import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import {FormBuilder, FormControl, FormGroup, Validators} from '@angular/forms';
import { first } from 'rxjs/operators';
import axios from "axios";
import {environment} from "../../enviroment";

@Component({
  selector: 'app-log-in-sign-up',
  templateUrl: './log-in-sign-up.component.html',
  styleUrls: ['./log-in-sign-up.component.css']
})
export class LogInSignUpComponent implements OnInit {
  // @ts-ignore
  userEmail: FormGroup ;
  showAlertInvalidEmail = false;
  showAlertInvalidPassword = false;
  showAlertRequired = false;
  showAlertDiferentPassword = false;
  constructor(private router: Router) {

    const email = document.getElementById("email_signin")!;
    const password = document.getElementById("password_signin")!;
  }

  ngOnInit(): void {
    this.userEmail = new FormGroup({
      email: new FormControl('', [
        Validators.required,
        Validators.pattern("^[a-zA-Z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$")]),
      password: new FormControl('', [
        Validators.required,
        Validators.pattern('(?=\\D*\\d)(?=[^a-z]*[a-z])(?=[^A-Z]*[A-Z]).{8,30}')])
    })
    const signUpButton = document.getElementById('signUp')!;
    const signInButton = document.getElementById('signIn')!;
    const container = document.getElementById('container')!;

    signUpButton.addEventListener('click', () => {
      container.classList.add("right-panel-active");
    });

    signInButton.addEventListener('click', () => {
      container.classList.remove("right-panel-active");
    });
  }

  onClickHome(){
    // @ts-ignore
    this.$router.replace({path: '/', query: {}})
  }

  onClickForgot(){
    // @ts-ignore
    this.$router.replace({path: '/', query: {}})
  }

  onClickSignIn(){

    const path = environment.path + `/login`
    const parameters = {
      mail: (<HTMLInputElement>document.getElementById("email_signin")).value,
      password: (<HTMLInputElement>document.getElementById("password_signin")).value
    }
    axios.post(path, parameters)
      .then((res) => {
        // @ts-ignore
        localStorage.setItem('currentUser', JSON.stringify({ token: res.data.token}));
        this.router.navigate(['/home']);
        alert('USER LOGGED SUCCESSFULLY')
      })
      .catch((error) => {
        console.error(error)
        // @ts-ignore
        alert(error.response.data.message)
        //alert(error.response.data.message)
      })
  }

  onClickSignUp(){
    this.showAlertInvalidEmail = false;
    this.showAlertInvalidPassword = false;
    this.showAlertRequired = false;
    this.showAlertDiferentPassword = false;
    const password =  (<HTMLInputElement>document.getElementById("password-signup")).value
    const repeat_password =  (<HTMLInputElement>document.getElementById("rep-password-signup")).value
    if (this.emailUser!.errors?.required || this.passwordUser!.errors?.required){
      this.showAlertRequired = true;
    } else if (this.emailUser!.errors?.pattern) {
      this.showAlertInvalidEmail = true;
    }
    else if (this.passwordUser!.errors?.pattern) {
      this.showAlertInvalidPassword = true;
    }
    else if(password != repeat_password){
      this.showAlertDiferentPassword = true;
    }
    else{
       const path = environment.path + `/register`
       const parameters = {
        username: 'Undefined',
        mail: (<HTMLInputElement>document.getElementById("email-signup")).value,
        password: password,
        repeat_password: repeat_password
      }

      axios.post(path, parameters)
        .then((res) => {
          // @ts-ignore
          localStorage.setItem('currentUser', JSON.stringify({ token: res.data.token}));
          // @ts-ignore
          alert(res.data.message)


        })
        .catch((error) => {
          console.error(error)
          alert(error.response.data.message)
        })
    }
  }
  get passwordUser(){
    return this.userEmail.get('password')
  }
  get confirmPasswordUser(){
    const password =  (<HTMLInputElement>document.getElementById("password-signup")).value
    const repeat_password =  (<HTMLInputElement>document.getElementById("rep-password-signup")).value
    return !(password == repeat_password)
  }
  get emailUser(){
    return this.userEmail.get('email')
  }


}
