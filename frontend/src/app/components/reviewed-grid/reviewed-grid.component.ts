import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-reviewed-grid',
  templateUrl: './reviewed-grid.component.html',
  styleUrls: ['./reviewed-grid.component.css']
})
export class ReviewedGridComponent implements OnInit {

  p = [1,2,3,4,5,6,7,8];
  ratings = {1: 2, 2: 3, 3: 4, 4: 4, 5: 5, 6: 3, 7: 4, 8: 3}

  constructor() { }

  ngOnInit(): void {
  }

  ngAfterViewInit(): void{
    for(let i in this.ratings) {
      // @ts-ignore
      let rat = this.ratings[i];
      // Set width of stars-inner to percentage
      document.getElementById('starts-inner-' + i)!.style.width = String(40*Number(rat)-15);
      console.log(document.getElementById('starts-inner-' + i)!.style.width);
      // @ts-ignore
      console.log(i*100)
    }
  }
}
