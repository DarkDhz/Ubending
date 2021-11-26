import { Component, OnInit } from '@angular/core';
import * as $ from "jquery";
import {Router} from "@angular/router";

@Component({
  selector: 'app-particles-button',
  templateUrl: './particles-button.component.html',
  styleUrls: ['./particles-button.component.css']
})
export class ParticlesButtonComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit(): void {
    $('.hero-btn').click(function(){
      if(!$('.hero-btn').parent().hasClass('active')){
        $(this).parent().stop().addClass('active');
        setTimeout(function(){
          $('.hero-btn').parent().removeClass('active');
        }, 2000);
      }
    });
  }

  allProducts() {
    let my_router= this.router
    setTimeout(function () {my_router.navigate(['/products']);}, 2000)
  }

}
