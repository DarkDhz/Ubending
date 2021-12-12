import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-product-card',
  templateUrl: './product-card.component.html',
  styleUrls: ['./product-card.component.css']
})
export class ProductCardComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {

  }

  wishlistAnimation(num: number) {
    const heart = document.getElementById('heart-'+num);
    const like = document.getElementById('liketext-'+num);
    heart!.classList.toggle('press');
    like!.classList.toggle('press');
  }
}
