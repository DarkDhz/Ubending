import { Component, OnInit } from '@angular/core';
import * as $ from "jquery";
import {Router} from "@angular/router";
//import * as slick from 'slick-carousel';

@Component({
  selector: 'app-card-slider',
  templateUrl: './card-slider.component.html',
  styleUrls: ['./card-slider.component.css']
})
export class CardSliderComponent implements OnInit {

  slides = [
    {img: "https://ubending.s3.eu-west-3.amazonaws.com/cars.svg", title: 'Cars',id:1},
    {img: "https://ubending.s3.eu-west-3.amazonaws.com/bikes.svg", title: 'Bikes',id:2},
    {img: "https://ubending.s3.eu-west-3.amazonaws.com/toys.svg", title: 'Home',id:3},
    {img: "https://ubending.s3.eu-west-3.amazonaws.com/home.svg", title: 'Toys',id:4},
    {img: "https://ubending.s3.eu-west-3.amazonaws.com/sports.svg", title: 'Sports',id:5},
    {img: "https://ubending.s3.eu-west-3.amazonaws.com/technology.svg", title: 'Technology',id:6},
    {img: "https://ubending.s3.eu-west-3.amazonaws.com/video_game.svg", title: 'Videogames',id:7},
    {img: "https://ubending.s3.eu-west-3.amazonaws.com/shopping.svg", title: 'Clothes',id:8},
    {img: "https://ubending.s3.eu-west-3.amazonaws.com/plants.svg", title: 'Plants',id:9},
    {img: "https://ubending.s3.eu-west-3.amazonaws.com/books_music.svg", title: 'Books & Music',id:10},
    {img: "https://ubending.s3.eu-west-3.amazonaws.com/cinema.svg", title: 'Cinema',id:11},
    {img: "https://ubending.s3.eu-west-3.amazonaws.com/pet_adoption.svg", title: 'Pet adoption',id:12}
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
  constructor(private router: Router) { }

  ngOnInit(): void {

  }
  redirectCategory(idCategory:number){
    localStorage.setItem('category', JSON.stringify(idCategory));
    this.router.navigate(['/products']);

  }

}


