import React, { useEffect } from "react"
import { Link } from "react-router-dom";
import PagetabComponent from "../../Components/Pagetab/Pagetab.component";
import PagebaseMiddleware from "../../Middlewares/Pagebase/Pagebase.middleware";
import "./Home.page.css";


let tabItemData = [
  {to:"/", content: 'Home'  },
  {to:"/contests", content: 'Contests'  },
  {to:"/problemset", content: 'Problems'  },
  {to:"/about", content: 'About'  },
  
]
function HomePage() {


  useEffect(() => {
    // For declaring Title
    document.title = 'Home - Redesigned OJ';
  });

    return <PagebaseMiddleware>
    <h2  className="title is-3"  style={{margin:0}}>Home Page</h2>
      <PagetabComponent tabItems={tabItemData} />
          <hr />
        
        <ul>
          <li>Problem set</li>
          <li>Contests</li>
          <li>Blogs</li>
          <li>About</li>
        </ul>

        <Link to="/createproblem">Create Problem</Link>
    </PagebaseMiddleware>;
  }
export default HomePage   