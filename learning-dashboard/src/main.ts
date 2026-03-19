import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { AppModule } from './app/app.module';
import {MatIconModule} from '@angular/material/icon';
import {MatDividerModule} from '@angular/material/divider';
import {MatButtonModule} from '@angular/material/button';
 imports: [MatButtonModule, MatDividerModule, MatIconModule]
platformBrowserDynamic().bootstrapModule(AppModule)
  .catch(err => console.error(err));
 