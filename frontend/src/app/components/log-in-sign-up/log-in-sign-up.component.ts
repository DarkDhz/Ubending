import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';
import axios from "axios";

@Component({
  selector: 'app-log-in-sign-up',
  templateUrl: './log-in-sign-up.component.html',
  styleUrls: ['./log-in-sign-up.component.css']
})
export class LogInSignUpComponent implements OnInit {

  @Output() messageEvent = new EventEmitter<string>();

  constructor() {
    const email = document.getElementById("email_signin")!;
    const password = document.getElementById("password_signin")!;
  }

  ngOnInit(): void {
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
    //const path = `https://ubending4.herokuapp.com/login`

    const path = `http://127.0.0.1:5000/login`
    const parameters = {
      mail: (<HTMLInputElement>document.getElementById("email_signin")).value,
      password: (<HTMLInputElement>document.getElementById("password_signin")).value
    }
    axios.post(path, parameters)
      .then((res) => {
        // @ts-ignore
        localStorage.setItem('currentUser', JSON.stringify({ token: res.data.token}));
        alert('USER LOGGED SUCCESSFULLY')
      })
      .catch((error) => {
        console.error(error)
        alert('ERROR LOGGING USER')
        //alert(error.response.data.message)
      })
  }

  onClickSignUp(){
    const path = `https://ubending4.herokuapp.com/register`
    // const path = `http://127.0.0.1:5000/register`
    const parameters = {
      username: 'Undefined',
      mail: (<HTMLInputElement>document.getElementById("email-signup")).value,
      password: (<HTMLInputElement>document.getElementById("password-signup")).value,
      repeat_password: (<HTMLInputElement>document.getElementById("rep-password-signup")).value
    }
    axios.post(path, parameters)
      .then((res) => {
        console.log('hola')
        // @ts-ignore
        alert(res.data.message)
      })
      .catch((error) => {
        console.error(error)
        alert(error.response.data.message)
      })
  }


}
