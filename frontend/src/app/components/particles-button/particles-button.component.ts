import { Component, OnInit } from '@angular/core';
import * as $ from "jquery";

@Component({
  selector: 'app-particles-button',
  templateUrl: './particles-button.component.html',
  styleUrls: ['./particles-button.component.css']
})
export class ParticlesButtonComponent implements OnInit {

  constructor() { }

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

}
