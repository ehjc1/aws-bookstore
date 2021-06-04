import React from 'react';
import Adapter from 'enzyme-adapter-react-16';
import { shallow, configure } from 'enzyme';
import PastPurchases from '../pastPurchases';
configure({ adapter: new Adapter() });

const headingText = 'Past purchases';

test('Check BestSellers render with correct heading', () => {
    // Render a checkbox with label in the document
    const pastPurchases = shallow(<PastPurchases />);
    expect(pastPurchases.find('h3').at(0).text()).toEqual(headingText);
});