import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditGradeComponent } from './edit-grade.component';

describe('EditGradeComponent', () => {
  let component: EditGradeComponent;
  let fixture: ComponentFixture<EditGradeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EditGradeComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(EditGradeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
