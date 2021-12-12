import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router";

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css']
})

export class SearchBarComponent implements OnInit {

  isLogged = false;
  isCollapsed = true;
  token = "null";

  constructor(private router: Router) {
    const currentUser = JSON.parse(<string>localStorage.getItem('currentUser'));
    if (currentUser != null) {
      this.token = currentUser.token;
      this.isLogged = true;
    }
  }


  ngOnInit(): void {
  }

  onClickSignIn(){
    // @ts-ignore
    this.$router.replace({path: '/', query: {}})
  }

  menuToggle(){
    const toggleMenu = document.querySelector('.menu')
    toggleMenu!.classList.toggle('active')
  }

  resetToken() {
    localStorage.removeItem('currentUser')
    this.router.navigate(['/login-signup'])
  }

  myProducts() {
    this.router.navigate(['/user-products'])
  }

  editProfile() {
    this.router.navigate(['/user-profile'])
  }

  wishlist() {
    this.router.navigate(['/wishlist'])
  }

  goToProducts() {
    this.router.navigate(['/products'])

  }


}
