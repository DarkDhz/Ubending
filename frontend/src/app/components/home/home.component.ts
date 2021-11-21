import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  isLogged = false;
  token = "null";

  constructor() {
    const currentUser = JSON.parse(<string>localStorage.getItem('currentUser'));
    if (currentUser != null) {
      this.token = currentUser.token;
      this.isLogged = true;
    }
    console.log("token:" +this.token)
  }

  ngOnInit(): void {
  }

  onClickSignIn(){
    this.isLogged = true
    // @ts-ignore
    this.$router.replace({path: '/', query: {}})
  }

  menuToggle(){
    const toggleMenu = document.querySelector('.menu')
    toggleMenu!.classList.toggle('active')
  }

}
