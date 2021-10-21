import {Component, OnInit} from '@angular/core';
import axios from 'axios'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit{
  title = 'frontend';
  products = [{"name":"AAA","price":40}];
  constructor() {
    this.getShows()
  }

  ngOnInit() {
  }
  getShows(){
    const path = 'http://127.0.0.1:5000/user/1/products'
    axios.get(path)
      .then((res) => {
        this.products =  res.data
        console.log(this.products)
      })
      .catch((error) => {
        console.error(error)
      })
  }
  url:string = "../assets/img2.jpg"

  changeImage(event:any){
    this.url = event.target.src;
  }

}


