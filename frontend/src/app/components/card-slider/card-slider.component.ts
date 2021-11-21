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
    {img: "../../../assets/cars.svg", title: 'Cars'},
    {img: "../../../assets/bikes.svg", title: 'Bikes'},
    {img: "../../../assets/toys.svg", title: 'Toys'},
    {img: "../../../assets/home.svg", title: 'Home'},
    {img: "../../../assets/sports.svg", title: 'Sports'},
    {img: "../../../assets/technology.svg", title: 'Technology'},
    {img: "../../../assets/video_game.svg", title: 'Videogames'},
    {img: "../../../assets/shopping.svg", title: 'Clothes'},
    {img: "../../../assets/plants.svg", title: 'Plants'},
    {img: "../../../assets/books_music.svg", title: 'Books & Music'},
    {img: "../../../assets/cinema.svg", title: 'Cinema'},
    {img: "../../../assets/pet_adoption.svg", title: 'Pet adoption'}
  ];
  slideConfig = {
    "slidesToShow": 4,
    "slidesToScroll": 2,
    "dots": true,
    "autoplay": true,
    "adaptiveHeight": false
  };

  slickInit(e: any) {
    console.log('slick initialized');
  }

  breakpoint(e: any) {
    console.log('breakpoint');
  }

  afterChange(e: any) {
    console.log('afterChange');
  }

  beforeChange(e: any) {
    console.log('beforeChange');
  }
  constructor() { }

  ngOnInit(): void {

  }

}


