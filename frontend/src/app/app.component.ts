import {Component, OnInit} from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'frontend';

  constructor() {
  }

  ngOnInit() {
  }

  url:string = "../assets/img2.jpg"

  changeImage(event:any){
    this.url = event.target.src;
  }

}


