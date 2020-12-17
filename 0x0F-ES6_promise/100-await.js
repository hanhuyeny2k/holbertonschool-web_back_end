import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  let photo;
  let user;

  try {
    [photo, user] = await Promise.all([uploadPhoto(), createUser()]);
  } catch (e) {
    photo = null;
    user = null;
  }
  return {
    photo,
    user,
  };
}
