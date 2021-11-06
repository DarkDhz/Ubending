import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-delete-item',
  templateUrl: './delete-item.component.html',
  styleUrls: ['./delete-item.component.css']
})

export class DeleteItemComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {

  }

  deleteProduct(){

  }

  closeDeleteAlert(){
    // @ts-ignore
    popup.classList.remove('active');
    // @ts-ignore
    overlay.classList.remove('active');
  }

}
