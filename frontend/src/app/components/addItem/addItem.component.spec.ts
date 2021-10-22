import { ComponentFixture, TestBed } from '@angular/core/testing';

import { addItemComponent } from './addItem.component';

describe('Prova2Component', () => {
  let component: addItemComponent;
  let fixture: ComponentFixture<addItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ addItemComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(addItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
