In = imread('edges.png');
In(120:170,190:270) = 0;

%%
figure(1);
[Xpos Ypos] = meshgrid(1:size(In,2), 1:size(In,1));
Edges = find(In > 0);
meas = [Xpos(Edges) Ypos(Edges)];

plot(meas(:,1), -meas(:,2), '.')
axis equal;

TopLines = meas(find(meas(:,2) < 5),:);
TopCenter = (min(TopLines(:,1)) + max(TopLines(:,1))) / 2;
Center = (min(meas(:,1)) + max(meas(:,1))) / 2;
BottomCenter = Center;
Mid = (TopCenter + BottomCenter) / 2;

% Left side
measLeft = meas(find(meas(:,1) < Mid),:);

hold on;
plot(measLeft(:,1), -measLeft(:,2), 'r.')
hold off;
axis equal;

measRight = meas(find(meas(:,1) > Mid),:);

hold on;
plot(measRight(:,1), -measRight(:,2), 'g.')
hold off;
axis equal;

%%
% p = polyfit(measLeft(:,1), measLeft(:,2), 2)
% 
% x1 = linspace(1,size(In,2));
% y1 = polyval(p,x1);
% hold on
% plot(x1,-y1)
% hold off
% 
axis equal;
xlim([0 460])
ylim([-180 0])

%% Perform RANSAC for estimation of parameters for Polynomial fit
% Swap x and y axis for better estimation
measLeft = [measLeft(:,2) measLeft(:,1)];
measRight = [measRight(:,2) measRight(:,1)];

ThetaLeft = PolynomialRANSAC(measLeft, 10, 10, 500);
ThetaRight = PolynomialRANSAC(measRight, 10, 10, 500);

%%
figure(2);
y1 = linspace(1,size(In,1),size(In,1));
x1 = polyval(ThetaLeft',y1);
plot(measLeft(:,2), -measLeft(:,1), 'r.')
hold on
plot(x1, -y1)
%plot(modelEvalX, -modelEvalY);
%plot(inliers(:,1), -inliners(:,2), 'gx')
hold off
axis equal;
xlim([0 460])
ylim([-180 0])

%%
figure(3);
y1 = linspace(1,size(In,1),size(In,1));
x1 = polyval(ThetaRight',y1);
plot(measRight(:,2), -measRight(:,1), 'g.')
hold on
plot(x1, -y1)
%plot(modelEvalX, -modelEvalY);
%plot(inliers(:,1), -inliners(:,2), 'gx')
hold off
axis equal;
xlim([0 460])
ylim([-180 0])