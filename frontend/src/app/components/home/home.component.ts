import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router";
import {environment} from "../../enviroment";
import axios from "axios";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  isLogged = false;
  token = "null";
  username = "";
  location = "";

  constructor(private router: Router) {
    const currentUser = JSON.parse(<string>localStorage.getItem('currentUser'));
    if (currentUser != null) {
      this.token = currentUser.token;
      this.isLogged = true;
    }
    const name = JSON.parse(<string>localStorage.getItem('username'));
    const loc = JSON.parse(<string>localStorage.getItem('location'));

    if ((name != null) && (loc != null)) {
      this.username = "" + name.user
      this.location = "" + loc.loc
    } else {
      const path = environment.path + `/api/userinfo/` + this.token
      axios.get(path)
      .then((res) => {
        // @ts-ignore
        let usr = res.data.username
        localStorage.setItem('username', JSON.stringify({ user: usr}));
        this.username = "" + usr

        // @ts-ignore
        let lc = res.data.location

        if (lc != null) {
          // @ts-ignore
          localStorage.setItem('location', JSON.stringify({ loc: lc}));
          this.location = "" + lc
        } else {
          // @ts-ignore
          localStorage.setItem('location', JSON.stringify({ loc: "No location"}));
          this.location = "No location"
        }


      })
      .catch((error) => {
        console.error(error)
      })
    }

  }

  ngOnInit(): void {
  }

  onClickSignIn(){
    // @ts-ignore
    this.$router.replace({path: '/', query: {}})
  }

  onClickReviews() {
    this.router.navigate(['/reviews'])
  }

  onClickProducts() {
    this.router.navigate(['/products'])
  }

  menuToggle(){
    const toggleMenu = document.querySelector('.menu')
    toggleMenu!.classList.toggle('active')
  }

  resetToken() {
    localStorage.removeItem('currentUser')
    localStorage.removeItem('username')
    localStorage.removeItem('location')
    this.router.navigate(['/login-signup'])
  }

  myProducts() {
    this.router.navigate(['/user-products'])
  }

  wishlist() {
    this.router.navigate(['/wishlist'])
  }

  editProfile() {
    this.router.navigate(['/user-profile'])
  }

}
