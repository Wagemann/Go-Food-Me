import React, {useState, useEffect} from "react";
import { NavLink } from 'react-router-dom';
import { Link } from 'react-router-dom';
import Card from "./Card.jsx";


function ListFundraisers() {
  const [post, setPost] = useState([]);
  
  useEffect(() => {
    async function getPost() {
      const url = process.env.REACT_APP_FastAPI_posts
      const POSTURL = url + "/api/post"
      const response = await fetch(POSTURL);
      if (response.ok) {
        const data = await response.json();
        setPost(data);
      } else {
        console.log("Response failed")
      }
    }
    getPost();
  }, [setPost] );

  return (
  <>
  <div className="position-relative">
  <NavLink to={"/post-form"}><button type="button" className="m-3 btn-lg btn-outline-success center">Create Fundraiser</button></NavLink>
  </div>
    <div className="row">
      {post.map(p => {
        console.log(p);
        return (
          <div className="col">
            <Link style={{textDecoration: 'none' }} to ={`/list-fundraisers/fundraisers/${p.id}`}>
              <Card
                title={p.title}
                created={p.created}
                description={p.description}
              />
            </Link>
          </div>
        )
      })}
    </div>
  </>
  )
}

export default ListFundraisers