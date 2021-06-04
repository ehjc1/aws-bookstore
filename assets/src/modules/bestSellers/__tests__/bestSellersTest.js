import React from 'react';
import Adapter from 'enzyme-adapter-react-16';
import { shallow, configure } from 'enzyme';
import BestSellers from '../bestSellers';
configure({ adapter: new Adapter() });

const headingText = 'Top 20 best sellers';

test('Check BestSellers render with correct heading', () => {
    // Render a checkbox with label in the document
    const bestSellers = shallow(<BestSellers />);
    expect(bestSellers.find('h3').text()).toEqual(headingText);
});