import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home-products',
  templateUrl: './home-products.component.html',
  styleUrls: ['./home-products.component.css']
})
export class HomeProductsComponent implements OnInit {

  products = [
    {img: "../../../assets/product1.png", title: 'Cacti Plant', price: '19.99€'},
    {img: "../../../assets/product2.png", title: 'Cactus Plant', price: '11.99€'},
    {img: "../../../assets/product3.png", title: 'Aloe Vera Plant', price: '7.99€'},
    {img: "../../../assets/product4.png", title: 'Succulent Plant', price: '5.99€'},
    {img: "../../../assets/product5.png", title: 'Succulent Plant', price: '10.99€'},
    {img: "../../../assets/product6.png", title: 'Green Plant', price: '8.99€'}
  ];

  constructor() { }

  ngOnInit(): void {
  }

}
