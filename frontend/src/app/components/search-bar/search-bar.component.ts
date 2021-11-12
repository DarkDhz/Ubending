import { Component, OnInit } from '@angular/core';
import {AppComponent} from "../../app.component";
import * as myGlobals from '../globals';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css']
})

export class SearchBarComponent implements OnInit {

  isLogged = false
  isCollapsed = true;

  constructor() {


  }
  ngOnInit(): void {
    // @ts-ignore
    console.log("TOKEN: " + AppComponent.token)

    if (myGlobals.token != 'null') {

      this.isLogged = true;
    }


  }

  onClickHome(){
    // @ts-ignore
    this.$router.replace({path: '/', query: {}})
  }

  onClickLogged(){
    this.isLogged = true
    // @ts-ignore
    this.$router.replace({path: '/', query: {}})
  }
  search(){
    alert('Implement search...')
  }

  filters(){
    alert('Implement filters...')
  }

  liked(){
    alert('Implement liked...')
  }

  chat(){
    alert('Implement chat...')
  }
  products(){
    alert('Implement products...')
  }
  profile(){
    alert('Implement profile...')
  }


}
