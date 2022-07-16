import React, { useEffect, useState } from "react"
import { Link } from "react-router-dom";
import PagetabComponent from "../../Components/Pagetab/Pagetab.component";
import PagebaseMiddleware from "../../Middlewares/Pagebase/Pagebase.middleware";
import "./CreateProblem.page.css";


let tabItemData = [
  {to:"/", content: 'Home'  },
  {to:"/contests", content: 'Contests'  },
  {to:"/problemset", content: 'Problems'  },
  {to:"/about", content: 'About'  },
  
]
function CreateProblemPage() {

    let [formState, setFormState] = useState({
        title: '',
        problemcode:'',
        description:'',
        difficulty: 'EASY',
        score: '',
        tags:[],
        testcases:[{ input: '', output: '' }]

    })
    useEffect(()=>{
        console.log(formState)
    },[formState]);

    let inputChange = (e)=>{
        let key = e.target.name;
        let val = e.target.value;
        if(key == "tags"){
            setFormState((prev)=>{
                return {
                    ...prev, [key]: [...prev.tags, val]
                }
            })
            return;
        }else{
            setFormState(prev=>{
                return {...prev, [key]:val}
            })

        }
    }

    let addTestcase = ()=>{
        setFormState((prev)=>{
            return {...prev, testcases: [...formState.testcases, { input: '', output: '' }]}
        })
    }
    let removeTestcase = (index)=>{
        setFormState((prev)=>{
            let arr = []
            formState.testcases.forEach((element,idx) => {
                if(idx != index){
                    arr.push(element)
                }
            });
            return {
                ...prev,
                testcases:arr
            }
        })
    }
    let onTestcaseInputChange = (e,index)=>{
        let key = e.target.name;
        let value = e.target.value;
        if(key == "input"){
            setFormState(prev=>{
                let arr = []
                prev.testcases.forEach((element,ei) => {
                    if(ei == index){
                        arr.push({ input: value, output: element.output})
                    }else{
                        arr.push(element)
                    }
                });


                return {
                    ...prev, 
                    testcases: arr
                }
            })
            return;
        }
        if(e.target.name =="output"){
            setFormState(prev=>{
                let arr = []
                prev.testcases.forEach((element,ei) => {
                    if(ei == index){
                        arr.push({ input: element.input, output: value})
                    }else{
                        arr.push(element)
                    }
                });

                
                return {
                    ...prev, 
                    testcases: arr
                }
            })
            return;
        }
    }


    let formSubmit = (e)=>{
        e.preventDefault();
    }
  useEffect(() => {
    // For declaring Title
    document.title = 'Create Problem - Redesigned OJ';
  },[]);

    return <PagebaseMiddleware>
    <h2  className="title is-3"  style={{margin:0}}>Create Problem Page</h2>
      <PagetabComponent tabItems={tabItemData} />
          <hr />
          <form onSubmit={formSubmit}>

          <div class="field">
            <label class="label">Problem Code *</label>
            <div class="control">
                <input class="input" type="text" placeholder="Enter Problem Code" name="problemcode" defaultValue={ formState.problemcode } required onChange={inputChange} />
                <small>Without space</small>
            </div>
            </div>


            <div class="field">
            <label class="label">Problem Title *</label>
            <div class="control">
                <input class="input" type="text" placeholder="Problem Title" name="title" defaultValue={ formState.title } required onChange={inputChange}/>
            </div>
            </div>


            <div class="field">
            <label class="label">Problem Description *</label>
            <div class="control">
                <textarea class="textarea" placeholder="Problem Description ... (Including Sample testcases here)" defaultValue={ formState.description } required name="description" onChange={inputChange}></textarea>
            </div>
            </div>


            <div class="field">
            <label class="label">Difficulty *</label>
            <div class="control">
                <div class="select">
                <select required name="difficulty" onChange={inputChange} defaultValue={ formState.difficulty }>
                    <option disabled unselectable="true">Select Difficulty Level</option>
                    <option value={"EASY"}>Easy</option>
                    <option value={"MEDIUM"}>Medium</option>
                    <option value={"HARD"}>Hard</option>
                </select>
                </div>
            </div>
            </div>


            <div class="field">
            <label class="label">Tags</label>
            <div class="control">
                <div class="select is-multiple">
                <select multiple name="tags" onChange={inputChange} defaultValue={ formState.tags }>
                    <option>Select Tags</option>
                    <option value={"DP"}>DP</option>
                    <option value={"GRAPH"}>Graph</option>
                </select>
                </div>
            </div>
            </div>

            
            <div class="field">
            <label class="label">Score *</label>
            <div class="control">
                <input className="input" type="number" placeholder="Please Enter Score " defaultValue={ formState.score } required name="score" onChange={inputChange} />
            </div>
            </div>



            <div className="subtitle">

            <div class="field">
                        <label class="label">Input Testcases *</label>
                        <div className="control">
                            <button className="button is-info " type="button" onClick={addTestcase}>Add Testcase</button>
                        </div>
                            {formState.testcases.map((eachtestcase, eachindex)=>{
                                return <>
                                <div className="" style={{border: "1px solid #dedede", borderRadius: "5px", padding: "20px", margin:"5px"}}> 
                                    <h3 className="subtitle is-3"> Testcase { eachindex}</h3>

                                    <div class="control">
                                        <div className="label">Input {eachindex}</div>
                                        <textarea class="textarea" placeholder="Input here" required name="input" onChange={(e)=>onTestcaseInputChange(e, eachindex)}></textarea>
                                    </div>
                                    <div class="control">
                                        <div className="label">Output {eachindex}</div>
                                        <textarea class="textarea" placeholder="Output Here" required name="output" onChange={(e)=>onTestcaseInputChange(e, eachindex)}></textarea>
                                    </div>
                                    <br />
                                    <button className="button is-danger" onClick={()=>removeTestcase(eachindex)}>Remove</button>

                                </div>
                                </>
                            })}
                        </div>

            </div>

            <div class="field is-grouped">
            <div class="control">
                <button class="button is-link">Create Problem Now</button>
            </div>
            <div class="control">
                <button class="button is-link is-danger" type="reset">Reset</button>
            </div>
            </div>
            
          </form>
          <br />
          <br />
    </PagebaseMiddleware>;
  }
export default CreateProblemPage   