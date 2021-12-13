import { Component, OnInit } from '@angular/core';
import axios from "axios";
import {Router} from "@angular/router";
import {environment} from "../enviroment";
import {UploadService} from "../services/upload.service";

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {

  token = "null";

  // @ts-ignore
  user_id : number;
  // @ts-ignore
  image_end: string;
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
  show = false;

  params = {};

  constructor(private router: Router, private uploadService: UploadService) {}

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
    const path = environment.path + `/api/userinfo/` + this.token
    axios.get(path)
      .then((res) => {
        // @ts-ignore
        this.name.value = res.data.username
        // @ts-ignore
        this.user_id = res.data.user_id
        // @ts-ignore
        this.image_end = res.data.userphoto
        if (this.image_end != 'null') {
          this.show = true
        }

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

  // @ts-ignore
  selectedFiles : FileList;

  upload(filename: String) {
    const file = this.selectedFiles.item(0);
    // @ts-ignore
    const extension = file.type.split('/').pop();
    this.uploadService.uploadFile(file, filename + "." + extension);
  }

  // @ts-ignore
  selectFile(event) {
    this.selectedFiles = event.target.files;
  }

  changeProfile(){
    const path = environment.path + `/api/userinfo/` + this.token
    this.showAlertError = false;
    if (this.selectedFiles == undefined) {
      this.params = {
        // @ts-ignore
        username: this.name.value,
        // @ts-ignore
        password: this.password.value,
        // @ts-ignore
        repeat_password: this.confirmPassword.value,
        // @ts-ignore
        location: this.position.value
      }
    } else {

      this.params = {
        // @ts-ignore
        username: this.name.value,
        // @ts-ignore
        password: this.password.value,
        // @ts-ignore
        repeat_password: this.confirmPassword.value,
        // @ts-ignore
        location: this.position.value,
        // @ts-ignore
        userphoto: this.selectedFiles.item(0).type.split('/').pop()
      }
    }


    axios.put(path, this.params)
      .then((res) => {
        alert('USER INFO UPDATED')
        if (this.selectedFiles != undefined) {
          this.uploadService.deleteFile("user"+this.user_id+"."+this.image_end)
          this.upload("user" + this.user_id)
        }
        localStorage.removeItem('username')
        localStorage.removeItem('location')
        this.router.navigate(['/home'])
      })
      .catch((error) => {
        this.showAlertError = true
        this.errorMessage = error.response.data.message
      })
  }

}
