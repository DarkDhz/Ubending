import { Component, OnInit } from '@angular/core';
import * as $ from "jquery";
//import * as slick from 'slick-carousel';

@Component({
  selector: 'app-card-slider',
  templateUrl: './card-slider.component.html',
  styleUrls: ['./card-slider.component.css']
})
export class CardSliderComponent implements OnInit {

  slides = [
    {img: "https://ubending.s3.eu-west-3.amazonaws.com/cars.svg", title: 'Cars'},
    {img: "https://ubending.s3.eu-west-3.amazonaws.com/bikes.svg", title: 'Bikes'},
    {img: "https://ubending.s3.eu-west-3.amazonaws.com/toys.svg", title: 'Toys'},
    {img: "https://ubending.s3.eu-west-3.amazonaws.com/home.svg", title: 'Home'},
    {img: "https://ubending.s3.eu-west-3.amazonaws.com/sports.svg", title: 'Sports'},
    {img: "https://ubending.s3.eu-west-3.amazonaws.com/technology.svg", title: 'Technology'},
    {img: "https://ubending.s3.eu-west-3.amazonaws.com/video_game.svg", title: 'Videogames'},
    {img: "https://ubending.s3.eu-west-3.amazonaws.com/shopping.svg", title: 'Clothes'},
    {img: "https://ubending.s3.eu-west-3.amazonaws.com/plants.svg", title: 'Plants'},
    {img: "https://ubending.s3.eu-west-3.amazonaws.com/books_music.svg", title: 'Books & Music'},
    {img: "https://ubending.s3.eu-west-3.amazonaws.com/cinema.svg", title: 'Cinema'},
    {img: "https://ubending.s3.eu-west-3.amazonaws.com/pet_adoption.svg", title: 'Pet adoption'}
  ];
  slideConfig = {
    "slidesToShow": 4,
    "slidesToScroll": 2,
    "dots": true,
    "autoplay": true,
    "adaptiveHeight": false
  };

  slickInit(e: any) {
  }

  breakpoint(e: any) {
  }

  afterChange(e: any) {
  }

  beforeChange(e: any) {
  }
  constructor() { }

  ngOnInit(): void {

  }

}


