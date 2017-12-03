close all
image = double(imread('car_art.jpg'));
image = image / max(image(:));

edge_magnitude = edge(rgb2gray(image), 'Canny', 0.25);

%%%%%%%%%%%

im = image;
yfilter = fspecial('sobel');
xfilter = yfilter';

edge_y = im;
edge_x = im;
for i = 1:3
    edge_x(:,:, i) = imfilter(im(:,:,i), xfilter);
    edge_y(:,:, i) = imfilter(im(:,:,i), yfilter);
end

Jx = sum(edge_x.^2, 3);
Jy = sum(edge_y.^2, 3);
Jxy = edge_x .* edge_y;

D = sqrt(abs(Jx.^2 - 2*Jx.*Jy + Jy.^2 + 4*Jxy.^2));
edge_magnitude = sqrt((Jx + Jy + D) / 2);

%%%%%%%%%%%%


figure, subplot(121), imshow(image)
subplot(122), imshow(edge_magnitude)