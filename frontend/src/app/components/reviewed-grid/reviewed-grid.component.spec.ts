import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ReviewedGridComponent } from './reviewed-grid.component';

describe('ReviewedGridComponent', () => {
  let component: ReviewedGridComponent;
  let fixture: ComponentFixture<ReviewedGridComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ReviewedGridComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ReviewedGridComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
