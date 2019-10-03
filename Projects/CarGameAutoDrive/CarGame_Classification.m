data = csvread('foo.csv')

data = data(find(data(:,1) == 1),:) % we should be driving for the data to make sense

idx_forward = find((data(:,2) == 0) & (data(:,3) == 0))
idx_left = find((data(:,2) == 1) & (data(:,3) == 0))
idx_right = find((data(:,2) == 0) & (data(:,3) == 1))

CenterTop = (data(:,4) + data(:,5)) / 2
CenterBottom = (data(:,6) + data(:,7)) / 2

figure(1);
plot(CenterTop(idx_forward), CenterBottom(idx_forward), 'r.');
hold on;
plot(CenterTop(idx_left), CenterBottom(idx_left), 'g.');
plot(CenterTop(idx_right), CenterBottom(idx_right), 'b.');
hold off;