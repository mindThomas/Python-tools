function Theta_result = PolynomialRANSAC(data, minInliers, errorThreshold, iterations)
%% Perform 5-point RANSAC
N = size(data,1);
Theta_best = [0,0,0];
Performance_best = 0;

for (n = 1:iterations)
% Step 1: Pick 5 random points
    r = ceil(rand(5,1)*N);
    points = data(r,:);
% Step 2: Estimate polynomial parameters based on these 5 points
    X = [points(:,1).^2, points(:,1), ones(5,1)];
    Y = points(:,2);
    X_inv = (X' * X)^-1 * X'; % compute psuedoinverse
    Theta = X_inv * Y; %  to find MSE estimate
    
% Step 3: Evaluate model parameters against the rest of the points in the dataset
    evalPoints = data;
    evalPoints(r,:) = []; % remove points used for estimation
    %modelEvalX = linspace(1,size(In,2),size(In,2))';
    modelEvalY = polyval(Theta', evalPoints(:,1));    
        
    error = (modelEvalY - evalPoints(:,2)) .^ 2;        
    
    inliers = [];
    for (i = 1:size(evalPoints,1))        
        if (error(i) < errorThreshold)
            inliers = [inliers; evalPoints(i,:)];
        end
    end
    
% Step 4: Compare with previous results  
    if (length(inliers) > minInliers)
        % We have a model which is likely a good match, now perform
        % parameter estimation with all points within inliner set and
        % the previous evaluation points
        points = [inliers; data(r,:)];
        X = [points(:,1).^2, points(:,1), ones(length(points),1)];
        Y = points(:,2);
        X_inv = (X' * X)^-1 * X'; % compute psuedoinverse
        Theta = X_inv * Y; %  to find MSE estimate
        
        % Calculate a total performance measure of how well this model fits
        % this point set (not the removed outliers)
        modelEvalY = polyval(Theta', points(:,1)); 
        error = (modelEvalY - points(:,2)) .^ 2;           
        %performance = sum(1./error);
        performance = length(inliers);
        
        if (performance > Performance_best)
            Theta_best = Theta;
            Performance_best = performance;            
%             fprintf('Performance %d\n', performance);
%             x1 = linspace(1,size(In,2));
%             y1 = polyval(Theta',x1);
%             figure(2);
%             plot(measLeft(:,1), -measLeft(:,2), 'r.')
%             hold on
%             plot(points(:,1), -points(:,2), 'gx');
%             plot(x1, -y1)
%             hold off;
%             pause;
        end
    end
end

Theta_result = Theta_best;