import * as React from 'react';
import { render } from 'react-dom';
import './index.css';
import WaterWave from '../../src';
import {useEffect, useRef, useState } from 'react';
const image: string = require('./assets/demo.jpg');

const Demo = () => {

  let [dropData, setdropData] = useState({});
  const dropRef = useRef(null);

  useEffect(() => {
    setInterval(async () => {
      const res = await fetch('http://127.0.0.1:5000/cordinates');
      const results = await res.json();
      if (results.length > 0) {
        results.map((data: any) => {
        dropData = {
          x: data[0],
          y: data[1],
          radius: 20,
          strength: 0.02
        }
        // @ts-ignore
          if(dropData?.x && dropData?.y) {
          setdropData(dropData);
          console.log(dropData);
        }
      })
      } else {
        setdropData({});
      }
      // @ts-ignore
      if(dropRef && dropRef.current && dropData?.x !== -1 && dropData?.y !== -1 && results !== []) {
        console.log('clicking')
        // @ts-ignore: Object is possibly 'null'.
        dropRef.current.click();
      }
    }, 1000);
  }, [])

  // @ts-ignore
  return (
      <WaterWave
        style={{ width: '100%', height: '100%', backgroundSize: 'cover' }}
        imageUrl={image}
        interactive={false}
      >
      {({drop}) => (
        <>
          <div onClick={() =>drop(dropData)} ref={dropRef} style={{display: "none"}}></div>
        </>
      )}
    </WaterWave>
  );
};

render(<Demo />, document.querySelector('#demo'));