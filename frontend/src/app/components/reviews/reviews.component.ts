import { Component, OnInit } from '@angular/core';
import {range} from "rxjs";
import {RatingComponent} from "../rating/rating.component";

// @ts-ignore
// @ts-ignore
@Component({
  selector: 'app-reviews',
  templateUrl: './reviews.component.html',
  styleUrls: ['./reviews.component.css']
})
export class ReviewsComponent implements OnInit {

  isLogged = false;
  // Total Stars
  starsTotal = 5;

  token = "null";

  // Score of each review (name os seller that has been reviewed)
  ratings = {
    'ana': {'total': 24, 'avg': 4.7, 'mine':5, '5stars': 8, '4stars': 13, '3stars': 2, '2stars': 1, '1stars': 0},
    'paco': {'total': 18, 'avg': 3.4, 'mine':4, '5stars': 3, '4stars': 13, '3stars': 2, '2stars': 1, '1stars': 0},
    'sara': {'total': 17, 'avg': 2.3, 'mine':3, '5stars': 1, '4stars': 13, '3stars': 2, '2stars': 1, '1stars': 0},
    'luis': {'total': 24, 'avg': 3.6, 'mine':3, '5stars': 8, '4stars': 13, '3stars': 2, '2stars': 1, '1stars': 0},
    'celia': {'total': 24, 'avg': 4.1, 'mine':2, '5stars': 8, '4stars': 13, '3stars': 2, '2stars': 1, '1stars': 0},
    'ramon': {'total': 16, 'avg': 1.7, 'mine':4, '5stars': 0, '4stars': 13, '3stars': 2, '2stars': 1, '1stars': 0},
    'alba': {'total': 19, 'avg': 0.4, 'mine':1, '5stars': 0, '4stars': 1, '3stars': 2, '2stars': 1, '1stars': 15}};


  constructor() {
    const currentUser = JSON.parse(<string>localStorage.getItem('currentUser'));
    if (currentUser != null) {
      this.token = currentUser.token;
      this.isLogged = true;
    }
  }

  ngOnInit(): void {
  }

  ngAfterViewInit(): void{

    /***************** NOT LOGGED USER VIEW *******************/

    for(let i in this.ratings){
      // Get percentage
      // @ts-ignore
      const avgStarPercentage = ((this.ratings)[i]['avg'] / this.starsTotal) * 100;

      // Round to nearest 10
      // This will be the width of starts
      const starPercentageRounded = `${Math.round(avgStarPercentage / 10) * 10}%`;

      // Set width of stars-inner to percentage
      document.getElementById('starts-inner-'+i)!.style.width = starPercentageRounded;
      // @ts-ignore
      //document.getElementById('mine-starts-inner-'+i)!.style.width = (this.ratings)[i]['mine'];

      // Add average rating
      // @ts-ignore
      document.getElementById('rating-score-'+i)!.innerHTML = (this.ratings)[i]['avg']+' out of 5';

      // Add total reviews for this seller
      // @ts-ignore
      document.getElementById('total-customers-'+i)!.innerHTML = (this.ratings)[i]['total']+' customers ratings';


      // STARS PERCENTAGES

      // @ts-ignore
      const star5Percentage = ((this.ratings)[i]['5stars'] / (this.ratings)[i]['total']) * 100;
      const rounded5 = `${Math.round(star5Percentage)}`;
      document.getElementById('5-stars-perc'+ i)!.innerHTML = rounded5+'%';
      (<HTMLProgressElement>document.getElementById('5-progress-bar'+i))!.value = Number(rounded5);


      // @ts-ignore
      const star4Percentage = ((this.ratings)[i]['4stars'] / (this.ratings)[i]['total']) * 100;
      const rounded4 = `${Math.round(star4Percentage)}`;
      document.getElementById('4-stars-perc'+ i)!.innerHTML = rounded4+'%';
      (<HTMLProgressElement>document.getElementById('4-progress-bar'+i))!.value = Number(rounded4);

      // @ts-ignore
      const star3Percentage = ((this.ratings)[i]['3stars'] / (this.ratings)[i]['total']) * 100;
      const rounded3 = `${Math.round(star3Percentage)}`;
      document.getElementById('3-stars-perc'+ i)!.innerHTML = rounded3+'%';
      (<HTMLProgressElement>document.getElementById('3-progress-bar'+i))!.value = Number(rounded3);

      // @ts-ignore
      const star2Percentage = ((this.ratings)[i]['2stars'] / (this.ratings)[i]['total']) * 100;
      const rounded2 = `${Math.round(star2Percentage)}`;
      document.getElementById('2-stars-perc'+ i)!.innerHTML = rounded2+'%';
      (<HTMLProgressElement>document.getElementById('2-progress-bar'+i))!.value = Number(rounded2);

      // @ts-ignore
      const star1Percentage = ((this.ratings)[i]['1stars'] / (this.ratings)[i]['total']) * 100;
      const rounded1 = `${Math.round(star1Percentage)}`;
      document.getElementById('1-stars-perc'+ i)!.innerHTML = rounded1+'%';
      (<HTMLProgressElement>document.getElementById('1-progress-bar'+i))!.value = Number(rounded1);

    }
  }

  setActiveLink(e: number){
    /*
    if (e == 0) {
      this.getProducts()
    } else {

    }*/
    const links = document.querySelectorAll('.nav-link');
    for(let i=0; i<links.length; i++){
      if(e==i){
        links[i].classList.add('active');
      }else{
        links[i].classList.remove('active');
      }

      if(e==0){
        document.getElementById('not-reviewed-grid')!.style.display = 'block';
        document.getElementById('reviewed-grid')!.style.display = 'none';

      } else if(e==1){
        document.getElementById('not-reviewed-grid')!.style.display = 'none';
        document.getElementById('reviewed-grid')!.style.display = 'block';
      }
    }
  }

}
