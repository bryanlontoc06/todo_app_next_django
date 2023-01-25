import Head from 'next/head'
import Image from 'next/image'
import { Inter } from '@next/font/google'
// import styles from '@/styles/Home.module.css'

const inter = Inter({ subsets: ['latin'] })

export default function Home({data, error}) {

  console.log(process.env.NEXT_PUBLIC_CLOUDINARY)
  return (
    <>
      {error && <p>{JSON.stringify(error)}</p> }
      {data.map((item, i) => {
        return (
          <div key={i}>
            <h1>{item.description}</h1>
            <p>Completed: {item.completed === true? 'True': 'False'}</p>
            <img src={process.env.NEXT_PUBLIC_CLOUDINARY + item.image} height={120} width={120} alt="" />
          </div>
        )
      })}
    </>
  )
}


export async function getStaticProps() {
  let data = [];
  let error = null;

  try {

      const response = await fetch(`${process.env.BASE_URL}/todo/`, {
      method: 'GET',
      // mode: 'cors', // no-cors, *cors, same-origin
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `token ${process.env.TOKEN}`
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      })

      data = await response.json()

    } catch (error) {
      console.log('Error =>', error);
      error = error.message ? error.message : "Something went wrong"
    }

    return {
      props: {
        data, 
        error
      }
    }

}