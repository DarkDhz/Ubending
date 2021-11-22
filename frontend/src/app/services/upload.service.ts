import { Injectable } from '@angular/core';
import * as S3 from 'aws-sdk/clients/s3';

@Injectable({
  providedIn: 'root'
})
export class UploadService {

  constructor() { }

  // @ts-ignore
  uploadFile(file, name) {
    const contentType = file.type;
    const bucket = new S3(
          {
              accessKeyId: 'AKIA4QL4BKU462D6VJOD',
              secretAccessKey: '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',
              region: 'eu-west-3'
          }
      );
      const params = {
          Bucket: 'ubending',
          Key: name,
          Body: file,
          ACL: 'public-read',
          ContentType: contentType
      };
      bucket.upload(params, function (err: any, data: any) {
          if (err) {
              console.log('There was an error uploading your file: ', err);
              return false;
          }
          console.log('Successfully uploaded file.', data);
          return true;
      });//for upload progress
/*bucket.upload(params).on('httpUploadProgress', function (evt) {
          console.log(evt.loaded + ' of ' + evt.total + ' Bytes');
      }).send(function (err, data) {
          if (err) {
              console.log('There was an error uploading your file: ', err);
              return false;
          }
          console.log('Successfully uploaded file.', data);
          return true;
      });*/
  }
  // @ts-ignore
  downloadFile(name) {
    const bucket = new S3(
          {
              accessKeyId: 'AKIA4QL4BKU462D6VJOD',
              secretAccessKey: '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',
              region: 'eu-west-3'
          }
      );
      const params = {
          Bucket: 'ubending',
          Key: name,
      };
      bucket.getObject(params, function (err: any, data: any) {
          if (err) {
              console.log('There was an error uploading your file: ', err);
              return false;
          }
          const string = new TextDecoder('utf-8').decode(data.Body);
          console.log(string);
          return true;
      });//for upload progress
/*bucket.upload(params).on('httpUploadProgress', function (evt) {
          console.log(evt.loaded + ' of ' + evt.total + ' Bytes');
      }).send(function (err, data) {
          if (err) {
              console.log('There was an error uploading your file: ', err);
              return false;
          }
          console.log('Successfully uploaded file.', data);
          return true;
      });*/
  }
}
