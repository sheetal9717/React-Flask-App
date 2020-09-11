
import React from 'react';
import logo from './logo.svg';
import './App.css';
import {Component} from 'react';

class App extends Component{
  
  constructor(props){
      super(props);
   
      this.state = {
        data: [],
        fetchedData: [],
        isLoading: true,
        error:null
      }
    }
   
    fetchData() {
        fetch('/country')
        .then(res => res.json())
        .then(json =>{
            this.setState({
              data: json,
              fetchedData : json,
              isLoading: false,
            })
        })
        .catch(error => this.setState({ error, isLoading: false }));
    }

    componentDidMount() {
        this.fetchData();
    }


onChangeHandler(e) {
  // console.log("+++++++++++++++++++");
  // console.log("in onChangehandler");
  // console.log(e.target.value);
  // console.log("+++++++++++++++++++");
  let newArray = this.state.data.filter((d)=>{
      let searchValue = d.country;
      // console.log("*****************");
      // console.log(searchValue);
      // console.log("*****************");      
      return searchValue.indexOf(e.target.value) !== -1;
  });
  // console.log("-------------------");
  // console.log(newArray)
  // console.log("-------------------");
  this.setState({
      fetchedData:newArray
  })
  
 
}

  render(){
    var { data, fetchedData, isLoading, error } = this.state;
    return(
         <div className="App">
           <header className="App-header">
              <img src={logo} className="App-logo" alt="logo" />
                <p>
                  Fetched Data from API :
                </p>
                    <input type="text" value={this.state.value} placeholder="Search by Country name..." onChange={this.onChangeHandler.bind(this)}/>
                    {error ? <p>{error.message}</p> : null}
                    <ol>
                    {!isLoading ? (
                        <ul>
                            {fetchedData.map(item => (
                            <li key = {item.id}>
                              Country : {item.country} | Country Code : {item.country_code} | Total Cases : {item.total_cases} | Recovered Cases : {item.recovered_cases} | Death Cases : {item.death_cases}
                            </li>
                            ))}
                        </ul>  
                    ) : (
                        <h3>Loading...</h3>
                    )}
                    </ol>
              

            </header>


          </div>
      );
      
   } 
  
}

export default App;