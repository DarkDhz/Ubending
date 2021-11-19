import { Component, OnInit } from '@angular/core';
import axios from "axios";
import {Router} from "@angular/router";

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {

  token = "null";

  // @ts-ignore
  name:object;
  // @ts-ignore
  position:object;
  // @ts-ignore
  password:object;
  // @ts-ignore
  confirmPassword:object;
  // @ts-ignore
  photo:object;

  user = {username: "LLUIS", password: "123456789Aa",confirmPassword: "123456789Aa",position: "08036"}
  showAlertError: Boolean = false;
  errorMessage = ''

  constructor(private router: Router) {}

  ngOnInit(): void {

    const currentUser = JSON.parse(<string>localStorage.getItem('currentUser'));
    if (currentUser != null) {
      this.token = currentUser.token;
    } else {
      alert('NOT LOGGED IN')
      this.router.navigate(['/home']);
    }

    // @ts-ignore
    this.name = document.getElementById('input_name')
    // @ts-ignore
    this.position = document.getElementById('input_position')
    // @ts-ignore
    this.password = document.getElementById('input_password')
    // @ts-ignore
    this.confirmPassword = document.getElementById('input_confirm')
    // @ts-ignore
    this.photo = document.getElementById('input_confirm')

    this.getUser();
  }

  getUser(){
    const path = `http://127.0.0.1:5000/api/userinfo/` + this.token
    axios.get(path)
      .then((res) => {
        // @ts-ignore
        this.name.value = res.data.username
        // @ts-ignore
        let loc = res.data.location

        if (loc != null) {
          // @ts-ignore
          this.position.value = loc
        } else {
          // @ts-ignore
          this.position.value = ""
        }
        // @ts-ignore
        this.password.value = ""
        // @ts-ignore
        this.confirmPassword.value = ""

      })
      .catch((error) => {
        console.error(error)
      })

  }

  changeProfile(){
    const path = `http://127.0.0.1:5000/api/userinfo/` + this.token
    this.showAlertError = false;
    const params = {
        // @ts-ignore
        username: this.name.value,
        // @ts-ignore
        password: this.password.value,
        // @ts-ignore
        repeat_password: this.confirmPassword.value,
        // @ts-ignore
        location: this.position.value
      }

    axios.put(path, params)
      .then((res) => {
        alert('USER INFO UPDATED')
        this.router.navigate(['/home'])
      })
      .catch((error) => {
        this.showAlertError = true
        this.errorMessage = error.response.data.message
      })
  }

  /*
  get password1(){
    // @ts-ignore
    return this.password?.value
  }

  get password2(){
    // @ts-ignore
    return this.confirmPassword?.value
  }

  validatePasswords(){// @ts-ignore
    if (this.password?.value != this.confirmPassword?.value){
      this.showAlertInvalid = false;
      this.showAlertDifferentPasswords = true;

    } else {
      // @ts-ignore
      if(this.name.value.length <1 || this.position.value.length <1 || this.password.value.length <1 || this.confirmPassword.value.length <1){
        this.showAlertInvalid = true;
        this.showAlertDifferentPasswords = false;
      }
      else{
        this.changeProfile()
      }


    }
  }
  */




}
