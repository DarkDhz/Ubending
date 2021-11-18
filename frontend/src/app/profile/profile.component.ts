import { Component, OnInit } from '@angular/core';
import axios from "axios";

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
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
  showAlertDifferentPasswords: Boolean = false;
  showAlertInvalid: Boolean = false;
  constructor() {}


  ngOnInit(): void {
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
    this.updateUser();
  }

  getUser(){
    const path = 'https://ubending3.herokuapp.com/user/1'
    axios.get(path)
      .then((res) => {
        // @ts-ignore
      })
      .catch((error) => {
        console.error(error)
      })
  }
  updateUser(){
    // @ts-ignore
    this.name.value= this.user.username
    // @ts-ignore
    this.position.value = this.user.position
    // @ts-ignore
    this.password.value = this.user.password
    // @ts-ignore
    this.confirmPassword.value = this.user.confirmPassword

  }

  changeProfile(){
    const path = 'https://ubending3.herokuapp.com/user/1'
    axios.put(path,this.user)
      .then((res) => {
        // @ts-ignore
      })
      .catch((error) => {
        console.error(error)
      })
  }
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



}
