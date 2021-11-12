import {Component, OnInit} from '@angular/core';
import axios from 'axios'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit{
  title = 'UBending';
  state = {products: []}
  public static token = '';

  constructor() {

  }

  ngOnInit() {
  }


}


